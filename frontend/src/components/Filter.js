import Form from 'react-bootstrap/Form';

const Filter = (props) => {

    const changeFilter = (event) => {
      props.setfilter(event.target.value)    
    }
    return (
      <>
        <div>
            Filter shown with 
            <Form.Control 
              value={props.filter} 
              onChange={changeFilter}/>
        </div>
      </>
  
    );
  }

export default Filter