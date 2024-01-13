import axios from 'axios'
const baseURL = 'http://127.0.0.1:8080/api/hospitals'

const getAll = () => {
    return axios.get(baseURL)
}

const getDetail = (id) => {
    return axios.get(`${baseURL}/${id}`)
}
const insert = (resource) => {
    return axios.post(baseURL, resource)
}

const update = (url,  newNote) => {
    return axios.put(url, newNote)
}

const destroy = (url) => {
    return axios.delete(url)
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