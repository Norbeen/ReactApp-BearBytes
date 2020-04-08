import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Socket } from './Socket';
import { Content } from './Content';
import { BrowserRouter, Route } from 'react-router-dom'

ReactDOM.render(
    <BrowserRouter>
          <Route path="/" component={Content}/>
     </BrowserRouter>,
    document.getElementById('content')
    );

Socket.on('connect', function() {
    console.log('Connecting to the server!');
});
