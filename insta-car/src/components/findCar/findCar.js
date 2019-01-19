import React from 'react'
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import "./findCar.css"
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';

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
            <Map google={this.props.google} zoom={14}>
                <Marker onClick={this.onMarkerClick}
                        name={'Current location'} />

                <InfoWindow onClose={this.onInfoWindowClose}>
                    <div>
                      <h1>{}</h1>
                    </div>
                </InfoWindow>
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
