import React from 'react'
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import "./findCar.css"
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';
var person = require('../assets/person.png');

class FindCar extends React.Component{
    constructor(props){
        super(props);
        this.state={
            vehicles:[]
        }
    }

    render(){
        return(
            <div>
            <Map google={this.props.google} zoom={16}
            initialCenter={{lat: 43.659466,lng: -79.396923}}>

            <Marker onClick={this.onMarkerClick} name={'Current location'}
            position={{lat: 43.659466,lng: -79.396923}}
            icon={{
      url: person,
      anchor: new this.props.google.maps.Point(32,32),
      scaledSize: new this.props.google.maps.Size(50,50)}}/>

            <Marker
            title={'The marker`s title will appear as a tooltip.'}
            name={'SOMA'}
            position={{lat: 44.659466,lng: -79.396923}} />

            </Map>
                <h1>Hello World</h1>
                {this.displayVehicles()}
            </div>
        )
    }

    displayVehicles(){
        console.log(this.state.vehicles);
    }

    componentDidMount(){
        this.getData()
        console.log(person);
    }

    async getData(){
        let url="http://localhost:8000/location"
        fetch(url).then(res=>res.json()).then(res=>{
            this.setState({vehicles:res}, console.log(this.state.vehicles))
        })
    }
}

export default GoogleApiWrapper({
  apiKey: ("AIzaSyDw7rz7Y3P2TO0vSWlJ1tGdlSgDtiV_ryE")
})(FindCar)
