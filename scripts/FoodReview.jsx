import * as React from 'react';
import { Socket } from './Socket';

function NavigationBar(props){
  return(
  <section className="navbar navbar-default navbar-fixed-top" role="navigation">
			<div className="container">
				<div className="navbar-header">
					<a href="#" className="navbar-brand">BearBites</a>
				</div>
				<div className="collapse navbar-collapse">
					<ul className="nav navbar-nav navbar-right">
						<li><a href="#home" >Rawlings Dining Hall</a></li>
						<li><a href="#gallery">Canteen</a></li>
					</ul>
				</div>
			</div>
		</section>
	)
}
function FoodCard(props){
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
    </div>)
    }
}