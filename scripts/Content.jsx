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
						<li><a href="/" >Rawlings Dining Hall</a></li>
						<li><a href="#gallery">Canteen</a></li>
					</ul>
				</div>
			</div>
		</section>
	)
}

function Rating(props){
  return(
    <div>
    <img src='https://i.ibb.co/qr7QcSn/4Rating.png' alt="Rating" style={{paddingBottom: "5%", width:"60%"}}/>
    </div>
    );
}

function FoodCard(props){
  return( 
  <a href="/review">
    <div className="w3-quarter" style={{paddingTop:"5%"}}>
      <div className="food-card">
      <img src={props.image} alt="Food Item" style={{width:"70%", paddingTop: "5%", objectFit: "cover"}}/>
      <h5 style={{color: "#F46311"}}>{props.title}</h5>
      <Rating 
        //rating={props.rating}
        />
    </div>
    </div>
  </a>
  )}

const breakfastHeader = <h3 className="food-time-header">Breakfast 7am-9am</h3>
const lunchHeader = <h3 className="food-time-header">Lunch 11am-2pm</h3>
const dinnerHeader = <h3 className="food-time-header">Dinner 4:30pm-8pm</h3>

export class Content extends React.Component { 
    constructor(props) {
    super(props);
    this.state = {
      'breakfast_data': [],
      'lunch_data': [],
      'dinner_data': []
    };
    
    this.componentDidMount = this.componentDidMount.bind(this)
    }
  componentDidMount() {
      Socket.on('menu loaded', (data) => {
            this.setState({
          'breakfast_data': data['breakfast_items'],
           'lunch_data': data['lunch_items'],
          'dinner_data' : data['dinner_items']
        });
      }
      )
      }

    render() {
        let breakfast_items = this.state.breakfast_data;
        let lunch_items = this.state.lunch_data;
        let dinner_items = this.state.dinner_data;

        return (
        <div>
		    <NavigationBar />
		
    	  {/*Creates margins for our page content */}
        <div className="w3-main w3-content w3-padding" style={{maxWidth:'1200px;margin-top:100px'}}>
        {/*Creates padding so title starts under navigation bar*/}
        <div style={{paddingTop: "40px"}}></div>
    

        {breakfastHeader}
        <div className="w3-row-padding w3-center">
        { breakfast_items.map ( bf_item =>
            <FoodCard 
             image={bf_item.bf_imageLink} title={bf_item.bf_title}
            // rating={bf_item.bf_averageRating}
            />
        )}
        </div>
        
       {lunchHeader}
      <div className="w3-row-padding w3-center">
       { lunch_items.map ( lunch_item =>
            <FoodCard 
             image={lunch_item.lunch_imageLink} title={lunch_item.lunch_title}
            //rating={lunch_item.lunch_averageRating}
            />
        )}
        </div>
        
        {dinnerHeader}
        <div className="w3-row-padding w3-center">
        { dinner_items.map ( dinner_item =>
          <FoodCard 
          image={dinner_item.din_imageLink} title={dinner_item.din_title} 
          //rating={dinner_item.din_averageRating}
          />
        )}
        </div>
      </div>
    </div>)
    }
}