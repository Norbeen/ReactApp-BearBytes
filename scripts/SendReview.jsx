import * as React from 'react';
import { Socket } from './Socket';


export class SendReview extends React.Component { 
    constructor(props) {
    super(props);
    this.state = {
      review: ""
    };
    
    this.handleReviewMessage = this.handleReviewMessage.bind(this);
  }
  
  handleReviewMessage(event) {
        this.setState({review: event.target.value});
        console.log('user_message', event.target.value);
    }
    
    render() {
        return (
    <div>
        <div className="w3-row">
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
        </div>
        <textarea name="" value = {this.state.review} className="review-form" placeholder="Type a review..." onChange = {this.handleReviewMessage}></textarea>
  		<div className="w3-row-padding">	
  			<button disabled= {/*!isEnabled */null} onClick={this.handleSubmit} className="review-button">Submit</button>
		</div>
    </div>)
    }
}