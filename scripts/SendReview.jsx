import * as React from 'react';
import { Socket } from './Socket';
import { Review } from './ReviewObject'
import { useState } from 'react';

function Stars(props){
    const [rating, updateRating] = useState(0);
    let count = 0
    let stars = [];
    
    const sendRating = (rate) => {
        Socket.emit('rating', {
    		'rating': rate
    	});
    }
    
    const updateRate = (rate) =>{
        if (rate == 1){
            updateRating(0)
            sendRating(0)
        }else{
            updateRating(rate)
            sendRating(rate)
        }
    }
    
    if (0<= rating <=5){
        for (var i = 0; i < rating; i++) {
            let current_count = count
            stars.push(
               <input key={count} src="https://i.ibb.co/VHTxrsd/oie-Ic-LCQTSqb-Kj6.png" 
               alt="Rating" 
               onClick={() =>{
                    updateRate(current_count+1)
                }}
               style={{width:"50px", height:"100%"}}
               type="image"
               />
                );
            count += 1;
            console.log("hi");
        }
        for (var i = 0; i < Math.abs(rating - 5 ); i++) {
            let current_count = count
            stars.push(
               <input key={count} src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" 
               alt="Rating" 
               onClick={() =>{
                    sendRating(current_count+1)
                    updateRating(current_count+1)
                }}
               style={{width:"50px", height:"100%"}}
               type="image"
               />
                );
        count += 1;
        console.log("hillo");
        }
    }
    console.log("stars",stars)

    return stars.map (star =>
               star
            )
        
    
}

export class SendReview extends React.Component { 
    constructor(props) {
    super(props);
    this.state = {
      review: "",
      user: null,
      loggedIn: false,
      rating: 0
    };
    
    this.handleReviewMessage = this.handleReviewMessage.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.componentDidMount = this.componentDidMount.bind(this)
    }
    
  componentDidMount() {
      Socket.on('logged in',(data) => {
      console.log('user signed in')
      this.setState({
        user: data['user']
      })
      this.setState({
        loggedIn: true
      })
    })
    Socket.on('review rating',(data) => {
      console.log('updated rating')
      this.setState({
        rating: data['rating']
      })
    })
  }
  
  handleSubmit(event){
    	event.preventDefault();
    	
    	let newReview = new Review(this.state.user, this.state.review, "", this.state.rating, "Jollof Rice", null);
    	this.state.review = newReview;
    	
    	Socket.emit('new review', {
    		'review': this.state.review
    	});
    	
    	this.setState({
    	    review: ''
    	});
        console.log('Sent a message to server!');
        console.log('User Review:', this.state.review);
    }
    
  canBeClicked(){
    console.log('logged:', this.state.loggedIn)
    const {review} = this.state;
    const {loggedIn} = this.state;
    return ((review.length > 0) && (loggedIn == true));
    }
  
  handleReviewMessage(event) {
        this.setState({review: event.target.value});
        console.log('review text:', event.target.value);
    }
    
    render() {
        let isEnabled = this.canBeClicked;
        return (
    <div>
        <div className="w3-row">
            <Stars />
        </div>
        <textarea name="" value = {this.state.review} className="review-form" placeholder="Type a review..." onChange = {this.handleReviewMessage}></textarea>
  		<div className="w3-row-padding">	
  			<button disabled= {/*isEnabled8*/null} onClick={this.handleSubmit} className="review-button">Submit</button>
		</div>
    </div>)
    }
}