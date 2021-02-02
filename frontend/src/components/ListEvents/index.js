import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import EventCard from '../EventCard';
import TopNav from '../TopNav';
import Off from '../Off';
import langs from '../../lang/lang';

import './index.css';

function ListEvents({ title, typeIcon, eventsArray, isRoute = false }) {

  const [lang, ] = useState(
    localStorage.getItem('lang') || 'en'
  );

  return (
    <div className="list-events-page">

      <TopNav title={title} typeIcon={typeIcon}/>
      <main className="list-events-cards-container">
          {
            eventsArray.length ?

            eventsArray.map(event => {
              if (isRoute) {
                return (
                  <Link to={{pathname: '/route/events', state: { parentId: event.uuid }}} key={event.uuid}>
                    <EventCard img={event.image} title={event.title} city={event.city}/>
                  </Link>
                )
              }
              return (
                <Link to={{pathname: '/detail', state: { eventId: event.uuid}}} key={event.uuid}>
                  <EventCard img={event.image} title={event.title} city={event.city}/>
                </Link>
              )
            })

            : 
                 
            <Off msg={langs['error'][lang].na} />      
          }
      </main>
    </div>
  );
}

export default ListEvents;