import * as React from 'react';
import { Socket } from './Socket';
import { Content } from './Content';
import { FoodReview } from './FoodReview';
import { BrowserRouter, Route, Switch } from 'react-router-dom'

export class Router extends React.Component { 
    
    render() {
        return (
        <BrowserRouter>
            <Switch>
                <Route path="/review" component={FoodReview}/>
                <Route path="/" component={Content}/>
            </Switch>
     </BrowserRouter>
     )
    }
}