import * as React from 'react';
import { Socket } from './Socket';

function StarRating(props){
  return(
    <img src="https://i.ibb.co/9hPds0L/2Rating.png" alt="Rating" style={{width:"50%"}}/>
    )
}

function ReviewCard(props){
  return( 
  <div className="w3-third" style={{paddingTop:"2%"}}>
    <div className="food-card">
      <div className="w3-row" >
        <div className="w3-col" style={{width:"40%"}} >
          <img src="https://i.pinimg.com/736x/ab/63/54/ab63547c6ecef3a4d542156532f5266e.jpg" alt="profile picture" style={{height: "80px", width:"80px", borderRadius: "50%", paddingTop: "5%", paddingBottom: "5%", objectFit: "cover", float:"right"}}/>
        </div>
        <div className="w3-col" style={{width:"60%"}}>
          <h5 style={{color: "#F46311"}}>Meorge Gartin</h5>
          <div className="w3-row">
            <img src="https://i.ibb.co/88Bp8w2/thumb-up-24px-1.png" alt="Rating" style={{width:"10%"}}/>
            <h7 style={{color: "#F46311", paddingRight:"10px"}}>10</h7>
            <img src="https://i.ibb.co/p4yrh6Z/thumb-down-24px-1.png" alt="Rating" style={{width:"10%"}}/>
            <h7 style={{color: "#F46311"}}>3</h7>
          </div>
            <img src="https://i.ibb.co/9hPds0L/2Rating.png" alt="Rating" style={{width:"50%"}}/>
        </div>
      </div>
      <div className="review-divider"/>
        <div className="w3-row" >
            <h6 style={{color: "#F46311"}}>04/16/2020</h6>
        </div>
        <p style={{color: "#F46311", width: "80%", marginLeft:"auto", marginRight: "auto", paddingTop: "2%"}}>dis chop de sweet me ehh. spiced well-well, eh di pass me correct. </p>
        <img src="https://gbc-cdn-public-media.azureedge.net/img82551.768x512.jpg" alt="Food Item" style={{width:"200px",height:"200px", paddingBottom: "5%", objectFit: "cover"}}/>
    </div>
  </div>
  )
}

export class ReviewsSection extends React.Component { 
    constructor(props) {
    super(props);
    this.state = {
      menu_data: []
    };
  }
    render() {
        return (
    <div>
        <div class="btn-group btn-group-toggle" data-toggle="buttons" style={{backgroundColor:"#F46311"}}>
            <label className="btn btn-secondary active segmented-control">
              <input type="radio" name="options" id="Newest" autocomplete="off" checked/> Newest
            </label>
            <label className="btn btn-secondary segmented-control">
              <input type="radio" name="options" id="popular" autocomplete="off"/> Most Popular
            </label>
            <label className="btn btn-secondary segmented-control">
              <input type="radio" name="options" id="positive" autocomplete="off"/> Most Positive
            </label>
            <label className="btn btn-secondary segmented-control">
              <input type="radio" name="options" id="critical" autocomplete="off"/> Most Critical
            </label>
        </div>
        <div className="w3-row-padding w3-center">
            <ReviewCard />
        </div>
    </div>)
    }
}