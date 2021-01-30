import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';

import Home from './pages/Home';
import Explore from './pages/Explore';
import Highlighted from './pages/Highlighted';
import Upselling from './pages/Upselling';
import RoutesP from './pages/Routes';
import EventDetail from './pages/EventDetail';
import RouteEvents from './pages/RouteEvents';

function Routes() {
  return (
    <BrowserRouter>
      <Route path="/" exact component={Home} />
      <Route path="/explore" component={Explore} />
      <Route path="/highlighted" component={Highlighted} />
      <Route path="/upselling" component={Upselling} />
      <Route path="/routes" component={RoutesP} />
      <Route path="/detail" component={EventDetail} />
      <Route path="/route/events" component={RouteEvents} />
    </BrowserRouter>
  );
}

export default Routes;