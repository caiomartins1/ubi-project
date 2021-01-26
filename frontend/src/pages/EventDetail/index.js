import React from 'react';
import L from 'leaflet';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import { Carousel } from 'react-bootstrap';
import TopNav from '../../components/TopNav';

import sampleImg from '../../assets/sample-card-img.png';
import locationIcon from '../../assets/icons/location-icon.png';
import exploreIcon from '../../assets/icons/explore-icon.png';
import directionsIcon from '../../assets/icons/directions-icon.png';

import 'leaflet/dist/leaflet.css';
import './index.css';

function EventDetail({ title, typeIcon}) {

  const locationIconLeaflet = L.icon({
    iconUrl: locationIcon,
  });

  return (
    <div className="event-detail-page">
      <TopNav title={'Attraction'} typeIcon={exploreIcon}/>

      <div className="event-detail-scroll">
        <div className="event-detail-info">
          <h1 className="event-detail-name">Helicopter Adventure, <br /> Addu City</h1>

          <h3 className="event-detail-description">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Labore modi beatae placeat nemo enim temporibus accusamus pariatur aspernatur. Vitae assumenda quasi nemo sed mollitia, dolore numquam quisquam eveniet impedit doloremque!</h3>
        </div>

        <div className="event-detail-location">
          <div className="event-detail-map">
            <MapContainer 
              center={[-0.6381564,73.1394224]} 
              zoom="4" 
              scrollWheelZoom={false}
              style={{height: "400px", width: "100%"}}
            >
              <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />

              <Marker position={[3.1097165,70.9964044]} icon={locationIconLeaflet}>
                <Popup>
                  Entry Point.
                </Popup>
              </Marker>

            </MapContainer>
          </div>
          <div className="event-detail-directions-buttom">
            <img src={directionsIcon} alt="" className="event-detail-directions-buttom-icon"/>
            <p className="event-detail-directions-buttom-title">Directions</p>
          </div>
        </div>

        <div className="event-detail-gallery">
          <h1 className="event-detail-gallery-title">Gallery</h1>
          <div className="event-detail-gallery-carousel">
            <Carousel>
              <Carousel.Item>
                <img
                  className="d-block w-100"
                  src={sampleImg}
                  alt="First slide"
                />
              </Carousel.Item>

              <Carousel.Item>
                <img
                  className="d-block w-100"
                  src={sampleImg}
                  alt="Third slide"
                />
              </Carousel.Item>

              <Carousel.Item>
                <img
                  className="d-block w-100"
                  src={sampleImg}
                  alt="Third slide"
                />
              </Carousel.Item>
            </Carousel>
          </div>
        </div>
      </div>
      
    </div>
  )
}

// https://www.google.com/maps/place/Addu+City,+Maldives/@-0.6415704,73.1542683,12z/data=!3m1!4b1!4m5!3m4!1s0x24b59ec91fa7961b:0xaf04ff732e934ada!8m2!3d-0.6300995!4d73.1585626

export default EventDetail;
