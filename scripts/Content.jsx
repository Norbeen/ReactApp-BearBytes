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

function Rating(props){
  return(
    <div>
    <img src={props.rating} alt="https://i.ibb.co/9hPds0L/2Rating.png" style={{paddingBottom: "5%", width:"60%"}}/>)
    </div>
    );
}

function FoodCard(props){
  return( 
  <div className="w3-row-padding w3-center">
    <div className="w3-quarter" style={{paddingTop:"5%"}}>
      <div className="food-card">
        <img src={props.image} alt="Food Item" style={{width:"70%", paddingTop: "5%"}}/>
        <h5 style={{color: "#F46311"}}> {props.title} </h5>
        <Rating rating={props.rating}/>
      </div>
    </div>
  </div>
  )
}

const breakfastHeader = <h3 className="food-time-header">Breakfast 7am-9am</h3>
const lunchHeader = <h3 className="food-time-header">Lunch 11am-2pm</h3>
const dinnerHeader = <h3 className="food-time-header">Dinner 4:30pm-8pm</h3>

export class Content extends React.Component { 
    constructor(props) {
    super(props);
    this.state = {
      menu_data: []
    };
  }
  componentDidMount() {
      Socket.on('menu loaded', (data) => {
        this.state.menu_data = data['menu_data'];
        this.SetState({
          'menu_data': this.state.menu_data
        });
      })
      }
      
    render() {
        let menu_items = this.state.menu_data;
        return (
        <div>
		    <NavigationBar />
		
    	{/*Creates margins for our cards */}
        <div className="w3-main w3-content w3-padding" style={{maxWidth:'1200px;margin-top:100px'}}>
       {/*Creates padding so title starts under navigation bar*/}
        <div style={{paddingTop: "40px"}}></div>
    
        {breakfastHeader}
        { menu_items.map ( item =>
            <FoodCard 
            title={item.title} image={item.imageLink} rating={item.rating}
            />
        )}  
        
       {lunchHeader}
        { menu_items.map ( item =>
            <FoodCard 
            title={item.title} image={item.imageLink} rating={item.rating}
            />
        )}
        
        {dinnerHeader}
        { menu_items.map ( item =>
          <FoodCard 
          title={item.title} image={item.imageLink} rating={item.rating}
          />
        )}
      </div>
    </div>)
    }
}