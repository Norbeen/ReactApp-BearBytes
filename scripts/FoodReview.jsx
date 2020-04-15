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
  <div className="w3-row-padding w3-center">
    <div className="w3-quarter" style={{paddingTop:"5%"}}>
      <div className="food-card">
        {/* TODO: need to replace the image and title with data from the json body */}
        <img src="https://whereismyspoon.co/wp-content/uploads/2018/07/jollof-rice-2.jpg" alt="Food Item" style={{width:"70%", paddingTop: "5%"}}/>
        <h5 style={{color: "#F46311"}}>Jollof Rice</h5>
        <img src="https://i.ibb.co/9hPds0L/2Rating.png" alt="Rating" style={{paddingBottom: "5%", width:"60%"}}/>
      </div>
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
        </div>
    </div>)
    }
}