import axios from 'axios';

const langApi = axios.create({
  baseURL: 'http://localhost:3000/lang',
});

export default langApi;