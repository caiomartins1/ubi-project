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

        {eventsArray.map(event => {
            return (
              <Link to="/detail" key={event.uuid}>
                <EventCard img={event.image} title={event.title} city={event.city}/>
              </Link>
            )
          })
        }

      </main>
    </div>
  );
}

export default ListEvents;
