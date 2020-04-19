import * as React from 'react';
import { Socket } from './Socket';
import { Review } from './ReviewObject'

export class SendReview extends React.Component { 
    constructor(props) {
    super(props);
    this.state = {
      review: ""
    };
    
    this.handleReviewMessage = this.handleReviewMessage.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  handleSubmit(event){
    	event.preventDefault();
    	let dummy_user = {
    	    name:"Meorge Gartin",
    	    profilepic:"https://i.pinimg.com/736x/ab/63/54/ab63547c6ecef3a4d542156532f5266e.jpg" 
    	}
    	
    	let newReview = new Review(dummy_user, this.state.review, "04/18/2020", 4, "Jollof Rice");
    	this.state.review = newReview;
    	
    	Socket.emit('new review', {
    		'review': this.state.review
    	});
    	
    	this.setState({
    	    review: ''
    	});
        console.log('Sent a message to server!');
        console.log('User Name:', dummy_user);
        console.log('User Review:', this.state.review);
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