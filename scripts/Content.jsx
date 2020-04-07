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

const breakfastHeader = <h3 className="food-time-header">Breakfast 7am-9am</h3>
const lunchHeader = <h3 className="food-time-header">Lunch 11am-2pm</h3>
const dinnerHeader = <h3 className="food-time-header">Dinner 4:30pm-8pm</h3>

export class Content extends React.Component {
    render() {
        return (<div>
        
		<NavigationBar />
		
		{/*Creates margins for our cards */}
    <div className="w3-main w3-content w3-padding" style={{maxWidth:'1200px;margin-top:100px'}}>
    
    {/*Creates padding so title starts under navigation bar*/}
    <div style={{paddingTop: "40px"}}></div>
    
    {breakfastHeader}
    <FoodCard />
    
    {lunchHeader}
    <FoodCard />

    
    {dinnerHeader}
    <FoodCard />
        
    </div>
    </div>)
    }
}