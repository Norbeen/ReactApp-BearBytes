import React from 'react';
 import { GoogleLogout } from 'react-google-login';
import { Socket } from './Socket'
/*global gapi*/

export class GoogleSignOut extends React.Component{
  constructor (props, context) {
    super(props, context);
  }

  responseGoogle () {
  Socket.emit('disconnect', {
      'disconnect':true
    });
    console.log("logged out")
  }

  render () {
    return (
      <GoogleLogout
        clientId="658977310896-knrl3gka66fldh83dao2rhgbblmd4un9.apps.googleusercontent.com"
        render={renderProps => (
            <button onClick={renderProps.onClick} disabled={renderProps.disabled} 
            style={{backgroundColor: "Transparent", color: "white", 
            border: "none", paddingTop:"15%", fontSize: "12px", lineHeight:"28px"}}>
              Sign Out
            </button>
          )}
        onSuccess={this.responseGoogle}
        onFailure={this.responseGoogle}
        />
    );
  }

}