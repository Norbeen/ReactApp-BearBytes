import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Socket } from './Socket';
import { Router } from './Router';

ReactDOM.render(
    <Router />,
    document.getElementById('content')
    );

Socket.on('connect', function() {
    console.log('Connecting to the server!');
});
