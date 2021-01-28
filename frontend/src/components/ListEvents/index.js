//TODO: Filter by active

import React from 'react';
import { Link } from 'react-router-dom';
import EventCard from '../EventCard';
import TopNav from '../TopNav';

import './index.css';

function ListEvents({ title, typeIcon, eventsArray }) {
  return (
    <div className="list-events-page">

      <TopNav title={title} typeIcon={typeIcon}/>

      <main className="list-events-cards-container">

        {
          eventsArray ?

          eventsArray.map(event => {
            return (
              <Link to={{pathname: '/detail', state: { eventId: event.uuid}}} key={event.uuid}>
                <EventCard img={event.image} title={event.title} city={event.city}/>
              </Link>
            )
          })

          : 
          
          <div className="no-events-available-container">
            <h1 className="no-events-available">
              {`No events available right now :(`}
            </h1>
          </div>
          
        }

      </main>
    </div>
  );
}

export default ListEvents;