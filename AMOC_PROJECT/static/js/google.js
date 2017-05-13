
  function onSignInCallback(resp) {
    gapi.client.load('plus', 'v1', apiClientLoaded);
    document.getElementById("myForm").submit;
  }

  /**
   * Sets up an API call after the Google API client loads.
   */
  function apiClientLoaded() {
    gapi.client.plus.people.get({userId: 'me'}).execute(handleEmailResponse);
  }

  /**
   * Response callback for when the API client receives a response.
   *
   * @param resp The API response object with the user email and profile information.
   */
  function handleEmailResponse(resp) {
    var primaryEmail;
    for (var i=0; i < resp.emails.length; i++) {
      if (resp.emails[i].type === 'account') primaryEmail = resp.emails[i].value;
    }
    document.getElementById('hid1').value = resp.image.url;
    document.getElementById('hid2').value = resp.displayName;
    document.getElementById('hid3').value = primaryEmail;
	document.getElementById('myform').submit();
      }
