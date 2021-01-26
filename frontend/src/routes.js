import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';

import Home from './pages/Home';
import Explore from './pages/Explore';
import Highlighted from './pages/Highlighted';
import Upselling from './pages/Upselling';
import RoutesP from './pages/Routes';
import EventDetail from './pages/EventDetail';

function Routes() {
  return (
    <BrowserRouter>
      <Route path="/" exact component={Home} />
      <Route path="/explore" component={Explore} />
      <Route path="/highlighted" component={Highlighted} />
      <Route path="/upselling" component={Upselling} />
      <Route path="/routes" component={RoutesP} />
      <Route path="/detail" component={EventDetail} />
    </BrowserRouter>
  );
}

export default Routes;