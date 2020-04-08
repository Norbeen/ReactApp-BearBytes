import * as React from 'react';
import { GoogleLogin } from 'react-google-login';
import { Socket } from './Socket';

/*global gapi*/

const responseGoogle = (response) => {
    // console.log("Hey, I am from GoogleSignin.js")
    // console.log(response.profileObj.name);
    // console.log(response.profileObj.imageUrl);
    // console.log(response.profileObj.email);
    // console.log("*************");
    // console.log(response);
    
    let auth = gapi.auth2.getAuthInstance();
    let user = auth.currentUser.get();
    if (user.isSignedIn()) {
        console.log("google token:  " + user.getAuthResponse().id_token);
        Socket.emit('google token', {
            'google_user_token': user.getAuthResponse().id_token
        });
    }
}

export class GoogleSignin extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isSignedIn : false,
            user_name : '',
            image_url : ''
        };
    }
    
    
    render() {
        return (
            <div>
                <GoogleLogin
                    clientId="651084917278-2tagl10k199e1a270rroovujhnt7eteh.apps.googleusercontent.com"
                    buttonText="Login"
                    onSuccess={responseGoogle}
                    onFailure={responseGoogle}
                    cookiePolicy={'single_host_origin'}
                   
                />
            </div>
        );
    }
}