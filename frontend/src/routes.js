import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';

import Home from './pages/Home';
import Explore from './pages/Explore';


function Routes() {
  return (
    <BrowserRouter>
      <Route path="/" exact component={Home} />
      <Route path="/explore" component={Explore} />
    </BrowserRouter>
  );
}

export default Routes;