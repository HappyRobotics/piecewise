// base imports
import React, { useEffect } from 'react';
import { ReactFormGenerator } from 'react-form-builder2';
import { css } from 'glamor';

// Bootstrap imports
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

// module imports
import NdtWidget from './utils/NdtWidget.jsx';

// custom styles
import './Survey.css';

export default function Survey(props) {
  const settings = props.location.state.settings;
  const locationConsent = props.location.state.locationConsent;
  const [form, setForm] = React.useState(null);
  const [location, setLocation] = React.useState({});
  const [results, setResults] = React.useState({});
  const [testsComplete, setTestsComplete] = React.useState(false);
  const [submitButton, setSubmitButton] = React.useState(null);

  // set colors
  let primary = css({
    color: settings ? settings.color_one : '#333',
  });

  let secondary = css({
    backgroundColor: `${settings ? settings.color_two : '#ccc'} !important`,
    borderColor: `${settings ? settings.color_two : '#ccc'} !important`,
  });

  const onFinish = (finished, results, location) => {
    if (finished) {
      setTestsComplete(true);
      setResults(results);
      setLocation(location);
    } else {
      setTestsComplete(false);
    }
  };

  const processError = errorMessage => {
    let text = `We're sorry your, request didn't go through. Please send the message below to the support team and we'll try to fix things as soon as we can.`;
    let debug = JSON.stringify(errorMessage);
    return [text, debug];
  };

  const uploadFormData = formData => {
    let status;
    fetch('/api/v1/submissions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data: { fields: formData } }),
    })
      .then(response => {
        status = response.status;
        return response.json();
      })
      .then(data => {
        if (status === 200 || status === 201) {
          props.history.push({
            pathname: '/thankyou',
            state: {
              location: location,
              results: results,
            },
          });
          return data;
        } else {
          let error = processError(data);
          throw new Error(`Error in response from server: ${error}`);
        }
      })
      .catch(error => {
        console.error('error:', error);
        throw Error(error.statusText);
      });
  };

  const downloadForm = () => {
    let status;
    return fetch('/api/v1/forms/latest', {
      method: 'GET',
    })
      .then(response => {
        status = response.status;
        return response.json();
      })
      .then(data => {
        if (status === 200 || status === 201) {
          return data;
        } else {
          let error = processError(data);
          throw new Error(`Error in response from server: ${error}`);
        }
      })
      .catch(error => {
        console.error('error:', error);
        throw Error(error.statusText);
      });
  };

  useEffect(() => {
    if (!form) {
      downloadForm()
        .then(res => {
          setForm(res.data[0].fields);
          setSubmitButton(document.querySelector('.btn-toolbar input'));
          return;
        })
        .catch(error => {
          console.error('error:', error);
        });
    }

    if (submitButton) {
      submitButton.classList.add('disabled');
      submitButton.disabled = true;
    }

    if (testsComplete) {
      submitButton.classList.remove('disabled');
      submitButton.disabled = false;
    }
  }, [testsComplete, form, submitButton]);

  if (!form) {
    return <div>Loading...</div>;
  } else {
    return (
      <Container className={'mt-4'}>
        {testsComplete ? (
          <div>You may now submit your survey to see your results.</div>
        ) : (
          <NdtWidget
            onFinish={onFinish}
            locationConsent={locationConsent}
          />
        )}
        <Row>
          <Col>
            <ReactFormGenerator
              answer_data={{}}
              form_method="POST"
              form_action="/api/v1/submissions"
              onSubmit={uploadFormData}
              data={form}
            />
          </Col>
        </Row>
      </Container>
    );
  }
}
