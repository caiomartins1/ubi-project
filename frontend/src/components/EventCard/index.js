import React from 'react';

import rightArrowIcon from '../../assets/icons/right-arrow-icon.png';
import locationIcon from '../../assets/icons/location-icon.png';

import './index.css';

function EventCard({ img, title, city }) {
  return (
    <div className="list-events-card">
      <img src={img} alt="" className="list-events-card-image"/>

      <div className="list-events-card-info">
        <p className="list-events-card-title">{`${title},`}</p>

        <div className="list-events-card-location-container">
          <div className="list-events-card-city-container">
            <img src={locationIcon} alt="" className="list-events-card-location-icon"/>
            <p className="list-events-card-city">{city}</p>
          </div>

          <img src={rightArrowIcon} alt="" className="list-events-card-right-arrow"/>
        </div>
      </div>
    </div>
  );
}

export default EventCard;
