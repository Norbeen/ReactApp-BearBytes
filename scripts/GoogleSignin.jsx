import React from 'react';
import { GoogleLogin } from 'react-google-login';
import { Socket } from './Socket'
/*global gapi*/

export class GoogleSignin extends React.Component{
  constructor (props, context) {
    super(props, context);
  }

  responseGoogle (googleUser) {
    let auth = gapi.auth2.getAuthInstance();
    let user = auth.currentUser.get();
    if(user.isSignedIn()) {
      console.log("google token" + user.getAuthResponse().id_token);
    }
    console.log("user:", googleUser)
  Socket.emit('google token', {
      'user_token':user.getAuthResponse().id_token
    });
  }

  render () {
    return (
      <div id="google-login">
      <GoogleLogin
          clientId="120440974471-c3v5k5h966i0jdei02gmut1gar1l1ple.apps.googleusercontent.com"
          render={renderProps => (
            <button onClick={renderProps.onClick} disabled={renderProps.disabled} 
            style={{backgroundColor: "Transparent", color: "white", 
            border: "none", paddingTop:"30%", fontSize: "12px", lineHeight:"28px"}}>
              SignIn
            </button>
          )}
          onSuccess={this.responseGoogle}
          onFailure={this.responseGoogle}
          cookiePolicy={'single_host_origin'}
        />
      </div>
    );
  }

}