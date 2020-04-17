import * as React from 'react';
import { Socket } from './Socket';

function NavigationBar(props){
  return(
  <section className="navbar navbar-default navbar-fixed-top" role="navigation">
			<div className="container">
				<div className="navbar-header">
					<a href="/" className="navbar-brand">BearBites</a>
				</div>
				<div className="collapse navbar-collapse">
					<ul className="nav navbar-nav navbar-right">
						<li><a href="/" >Rawlings Dining Hall</a></li>
						<li><a href="#gallery">Canteen</a></li>
					</ul>
				</div>
			</div>
		</section>
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
          <div className="w3-row">
            <h5 style={{color: "#F46311"}}>Meorge Gartin</h5>
          </div>
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



export class FoodReview extends React.Component { 
    constructor(props) {
    super(props);
    this.state = {
      menu_data: []
    };
  }
    render() {
        return (
        <div>
		    <NavigationBar />
  		  {/*Creates margins for our page content */}
        <div className="w3-main w3-content w3-padding" style={{maxWidth:'1200px;margin-top:100px'}}>
          {/*Creates padding so title starts under navigation bar*/}
          <div style={{paddingTop: "40px"}}></div>
          <div className="w3-row-padding w3-center">
            <div className="w3-half">
              <img src="https://whereismyspoon.co/wp-content/uploads/2018/07/jollof-rice-2.jpg" alt="Food Item" style={{width:"400px", height:"400px", paddingTop: "5%", objectFit: "cover"}} />
            </div>
            <div className="w3-half" style={{paddingTop: "150px"}}>
              <h1 className="food-time-header">Jollof Rice</h1>
              <h3 className="food-time-header">Servings/Calories: </h3>
              <img src="https://i.ibb.co/9hPds0L/2Rating.png" alt="Rating" style={{width:"40%", marginLeft: "auto", marginRight: "auto", display: "block"}}/>
              <h4 className="food-time-header">(0 reviews)</h4>
            </div>
          </div>
          <h1 className="food-review-header">Reviews</h1>
          <div style={{background:"#F46311", height:"15px", width:"100%"}}></div>
          <h4 className="food-review-header">Leave a Review</h4>
          <div className="w3-row">
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
            <img src="https://i.ibb.co/XJVKQz1/oie-Co-QW0a-GNUEAp.png" alt="Rating" style={{width:"50px", height:"100%"}}/>
          </div>
          <textarea name="" value = {this.state.user_message} className="review-form" placeholder="Type a review..." onChange = {this.handleChangeMessage}></textarea>
      		<div className="w3-row-padding">	
      			<button disabled= {/*!isEnabled */null} onClick={this.handleSubmit} className="review-button">Submit</button>
    			</div>
    			<div style={{ paddingTop:"3%"}} />
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
        </div>
    </div>)
    }
}