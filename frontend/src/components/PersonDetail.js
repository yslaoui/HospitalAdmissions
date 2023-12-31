import { useEffect, useState, React } from 'react'
import services from '../services/services'
import { useParams } from 'react-router-dom';

const PersonDetail = (props) => {

    let {id} = useParams();
    const [personDetail, setpersonDetail] = useState({ name: '', age: '' });

    useEffect(()=> {
        services
          .getDetail(id)
          .then(response => {
            console.log(response.data)
            setpersonDetail({
                name: response.data.name, 
                age: response.data.age,
                gender: response.data.gender
            })
          })
       }, [])

    return (
        <div>
            <h1> Person id: {id} </h1>
            <h1> Person name: {personDetail.name} </h1>
            <h1> Person age: {personDetail.age} </h1>
            <h1> Person gender: {personDetail.gender} </h1>
        </div>
    );
}


export default PersonDetail