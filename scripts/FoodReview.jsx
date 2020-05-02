import * as React from 'react';
import { Socket } from './Socket';
import { ReviewsSection } from './ReviewsSection'
import { SendReview } from './SendReview'
import { NavigationBar } from './Content'
import { GoogleSignOut } from './GoogleSignOut';
import { GoogleSignin } from './GoogleSignin';

function Rating(props){
  if(props.rating == 0){
    return(
      <img src="https://i.ibb.co/89PP1RD/0Rating.png" alt="Rating" style={{width:"40%", marginLeft: "auto", marginRight: "auto", display: "block"}}/>
      )
  } 
  
  if(props.rating == 1){
    return(
    <img src="https://i.ibb.co/9hPds0L/2Rating.png" alt="Rating" style={{width:"40%", marginLeft: "auto", marginRight: "auto", display: "block"}}/>
    )
  } 
  
  if(props.rating == 2){
    return(
    <img src="https://i.ibb.co/9hPds0L/2Rating.png" alt="Rating" style={{width:"40%", marginLeft: "auto", marginRight: "auto", display: "block"}}/>
    )
  } 
  
  if(props.rating == 3){
    return(
    <img src="https://i.ibb.co/1Rq3tcb/3Rating.png" alt="Rating" style={{width:"40%", marginLeft: "auto", marginRight: "auto", display: "block"}}/>
    )
  } 
  
  if(props.rating == 4){
    return(
    <img src="https://i.ibb.co/qr7QcSn/4Rating.png" alt="Rating" style={{width:"40%", marginLeft: "auto", marginRight: "auto", display: "block"}}/>
    )
  } 
  
  if(props.rating == 5){
    return(
    <img src="https://i.ibb.co/K97vCGR/5Rating.png" alt="Rating" style={{width:"40%", marginLeft: "auto", marginRight: "auto", display: "block"}}/>
    )
  }
  return(<h3 style={{color: "#0B76F4", width: "80%", marginLeft:"auto", marginRight: "auto"}}>(Rating unavailable)</h3>)
}

function FoodInformation(props){
  return(
    <div className="w3-row-padding w3-center">
            <div className="w3-half">
              <img src="https://whereismyspoon.co/wp-content/uploads/2018/07/jollof-rice-2.jpg" alt="Food Item" style={{width:"400px", height:"400px", paddingTop: "5%", objectFit: "cover"}} />
            </div>
            <div className="w3-half" style={{paddingTop: "150px"}}>
              <h1 className="food-time-header">{props.title}</h1>
              <h3 className="food-time-header">Calories per Serving: {props.nutri} </h3>
              <Rating rating={props.rating} />
              <h4 className="food-time-header">{props.reviewCount} review(s)</h4>
            </div>
          </div>
    )
}

const reviewHeader = <div>
            <h1 className="food-review-header">Reviews</h1>
            <div style={{background:"#F46311", height:"15px", width:"100%"}}></div>
            <h4 className="food-review-header">Leave a Review</h4>
          </div>

export class FoodReview extends React.Component { 
    constructor(props) {
    super(props);
    this.state = {
      menu_data: [],
      signIn: <GoogleSignin />
    };
  }
  
  componentDidMount() {
      Socket.on('logged in',(data) => {
        console.log('user signed in')
        this.setState({
          signIn: <GoogleSignOut />
        })
      })
      Socket.on('menu item',(data) => {
        console.log('received menu data')
        this.setState({
          menu_data: data['menu_item']
        })
      })
      
  }
  
    render() {
      let food = this.state.menu_data
        return (
    <div>
		  <NavigationBar signIn={this.state.signIn} />
  		{/*Creates margins for our page content */}
      <div className="w3-main w3-content w3-padding" style={{maxWidth:'1200px;margin-top:100px'}}>
      {/*Creates padding so title starts under navigation bar*/}
      <div style={{paddingTop: "40px"}}></div>
      <FoodInformation title={food.title} nutri={"1/2 cup(101.6 cal)"} rating={5} reviewCount={1}  />
      {reviewHeader}
      <SendReview />
  		<div style={{ paddingTop:"3%"}} />
  			<ReviewsSection />
      </div>
    </div>)
    }
}