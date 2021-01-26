import React from 'react';
import { Link } from 'react-router-dom';
import EventCard from '../EventCard';
import TopNav from '../TopNav';

import './index.css';

function ListEvents({ title, typeIcon }) {
  return (
    <div className="list-events-page">

      <TopNav title={title} typeIcon={typeIcon}/>

      <main className="list-events-cards-container">

        <Link to="/detail">
          <EventCard />
        </Link>
        <EventCard />
        <EventCard />
        <EventCard />
        <EventCard />
      </main>
    </div>
  );
}

export default ListEvents;
