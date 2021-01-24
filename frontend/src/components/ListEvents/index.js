import React from 'react';
import { Link } from 'react-router-dom';
import EventCard from '../EventCard';

import leftArrowIcon from '../../assets/icons/left-arrow-icon.png';


import './index.css';

function ListEvents({ title, typeIcon }) {
  return (
    <div className="list-events-page">
      <nav className="list-events-nav">
        <Link to="/">
          <img src={leftArrowIcon} alt="" className="list-events-nav-back-icon"/>
        </Link>

        <h1 className="list-events-nav-title">{title}</h1>

        <img src={typeIcon} alt="" className="list-events-nav-type-icon"/>
      </nav>

      <main className="list-events-cards-container">
        <EventCard />
        <EventCard />
        <EventCard />
        <EventCard />
        <EventCard />
      </main>
    </div>
  );
}

export default ListEvents;
