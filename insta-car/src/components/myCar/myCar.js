import React from 'react';
import Typography from '@material-ui/core/Typography';
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';

import './myCar.css'
var car = require('../assets/car.png');
class MyCar extends React.Component{
    constructor(props){
        super(props);
        this.state={
            vehicle_info:[]
        }
    }
    render(){
        return(
            <div className="centerItems">
            <Typography variant = "h2"
             color = "inherit" >
             {this.state.vehicle_info.year} {this.state.vehicle_info.make} {this.state.vehicle_info.model}
             </Typography>

             <img src={car} alt=""/>

            <div className="map">
                <Map google={this.props.google} zoom={16}
                initialCenter={{lat: 43.659466,lng: -79.396923}}>
                <Marker onClick={this.onMarkerClick} name={'Current location'}
                position={{lat: 43.659466,lng: -79.396923}}/>
                </Map>
            </div>
            </div>
        );
    }

    componentDidMount(){
        this.getInfo();
    }

    async getInfo(){
        let url = "https://www.mdshulman.com/smartcar/vehicle"
        fetch(url).then(res=>res.json()).then(res=>{
            console.log(res[0][1]);
            this.setState({vehicle_info:res[0][1]})
        })
    }
}

export default MyCar
