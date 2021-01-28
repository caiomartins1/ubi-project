//TODO: Filter by active

import React from 'react';
import { Offline, Online } from "react-detect-offline";
import { Link } from 'react-router-dom';
import EventCard from '../EventCard';
import TopNav from '../TopNav';
import Off from '../Off';

import './index.css';

function ListEvents({ title, typeIcon, eventsArray }) {
  return (
    <div className="list-events-page">

      <TopNav title={title} typeIcon={typeIcon}/>

      <Online>
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
      </Online>

      <Offline>
        <Off msg="Whooops! You need Internet connection to access this page :( "/>
      </Offline>
    </div>
  );
}

export default ListEvents;