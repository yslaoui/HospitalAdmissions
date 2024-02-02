import axios from 'axios'
import getCsrfToken from './csrfToken'

const baseURL = 'http://127.0.0.1:8080/api/doctors'


const getAll = () => {
    return axios.get(baseURL)
}

const getDetail = (id) => {
    return axios.get(`${baseURL}/${id}`)
}
const insert = (resource) => {
    const csrfToken = getCsrfToken();
    return axios.post(baseURL, resource, {
        headers: {'X-CSRFToken': csrfToken} 
     })
}

const update = (url,  newNote) => {
    const csrfToken = getCsrfToken();
    return axios.put(url, newNote, {
        headers: {'X-CSRFToken': csrfToken} 
     })
}

const destroy = (url) => {
    const csrfToken = getCsrfToken();
    return axios.delete(url, {
        headers: {'X-CSRFToken': csrfToken} 
     })
}


const printme = () => console.log(`Hello from services`)

export default {
    getAll: getAll,
    insert: insert, 
    update: update, 
    printme: printme,
    destroy: destroy, 
    getDetail: getDetail
}
