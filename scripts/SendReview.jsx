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
    
    Socket.on('send review',(data) => {
      console.log('reset')
      updateRating(0)
    })
    
    if (0<= rating <=5){
        for (var i = 0; i < rating; i++) {
            stars.push(
               <input key={count} src="https://i.ibb.co/VHTxrsd/oie-Ic-LCQTSqb-Kj6.png" 
               alt="Rating" 
               onClick={() =>{
                    updateRating(0)
                    sendRating(0)
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
      rating: 0,
      current_food_id: ""
    };
    
    this.handleReviewMessage = this.handleReviewMessage.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.componentDidMount = this.componentDidMount.bind(this)
    }
    
  componentDidMount() {
      this.setState({
        loggedIn: false
      })
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
    Socket.on('menu item',(data) => {
        console.log('received menu data in send review')
        this.setState({
          current_food_id: data['menu_item']["id"]
        });
      })
  }
  
  handleSubmit(event){
      const {loggedIn} = this.state;
      if (!loggedIn){
        alert("you must be logged in to write a review")
    }else{
    	event.preventDefault();
    	
    	let newReview = new Review(this.state.user, this.state.review, "", this.state.rating, this.state.current_food_id, null);
    	this.state.review = newReview;
    	
    	Socket.emit('new review', {
    		'review': this.state.review
    	});
    	
    	this.setState({
    	    review: ''
    	});
        console.log('Sent a message to server!');
        console.log('User Review:', this.state.review);
    }}
    
  
  handleReviewMessage(event) {
        this.setState({review: event.target.value});
        console.log('review text:', event.target.value);
    }
    
    render() {
        return (
    <div>
        <div className="w3-row">
            <Stars />
        </div>
        <textarea name="" value = {this.state.review} className="review-form" placeholder="Type a review..." onChange = {this.handleReviewMessage}></textarea>
  		<div className="w3-row-padding">	
  			<button onClick={this.handleSubmit} className="review-button">Submit</button>
		</div>
    </div>)
    }
}