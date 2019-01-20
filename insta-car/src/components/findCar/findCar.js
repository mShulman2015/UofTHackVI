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
            vehicles:[],
            positions:[]
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

            {this.displayVehicles()}

            </Map>
            </div>
        )
    }

    displayVehicles(){
        console.log(
            "holy fuck"
        );
        console.log(this.state.positions);
        return(
            <Marker position={this.state.positions[0]}/>
        )
    }

    componentDidMount(){
        this.getData()
        console.log(person);
    }

    sortData(){
        var position_curr = new Object();
        var positions = []
        let k = this.state.vehicles.map(element=>{
            console.log(element[1].data);
            position_curr = {lat:element[1].data.latitude, lng:element[1].data.longitude}
            positions.push(position_curr)
        })
        this.setState({positions:positions}, this.displayVehicles)
    }

    async getData(){
        let url = "https://www.mdshulman.com/smartcar/location"
        fetch(url).then(res=>res.json()).then(res=>{
            this.setState({vehicles:res}, this.sortData)
        })
    }

    async getPhoto(){
        let url = "https://www.mdshulman.com/smartcar/location"
        fetch(url).then(res=>res.json()).then(res=>{
            this.setState({vehicles:res}, this.sortData)
        })
    }
}

export default GoogleApiWrapper({
  apiKey: ("AIzaSyDw7rz7Y3P2TO0vSWlJ1tGdlSgDtiV_ryE")
})(FindCar)
