import { useEffect, useState, React } from 'react'
import patientServices from '../services/patientServices'
import { useParams } from 'react-router-dom';
import NavigationBar from './NavigationBar'

const PatientDetail = (props) => {

    let {id} = useParams();
    const [patientDetail, setpatientDetail] = useState({ name: '', age: '', gender: {}, blood_type: {}, medication: [] });

    useEffect(()=> {
        patientServices
          .getDetail(id)
          .then(response => {
            console.log(response.data)
            setpatientDetail({
                name: response.data.name, 
                age: response.data.age,
                gender: response.data.gender, 
                blood_type: response.data.blood_type,
                medication: response.data.medication
            })
          })
       }, [])

    return (
        <div>
            <NavigationBar/>  
            <h1> patient id: {id} </h1>
            <h1> name: {patientDetail.name} </h1>
            <h1> age: {patientDetail.age} </h1>
            <h1> gender: {patientDetail.gender["gender"]} </h1>
            <h1> blood type: {patientDetail.blood_type["blood_type"]} </h1>
            {patientDetail.medication.map(x => {
                return (
                    <div>
                        <h1> medication {x.medication} </h1>
                    </div>
                )
            })}
        </div>
    );
}


export default PatientDetail