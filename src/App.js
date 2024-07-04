import React, {useEffect} from 'react';
import Form from './components/Form';
import { useSelector, useDispatch } from 'react-redux';
import { fetchUsers } from './store/services/formSlice';

function App() {
  const dispatch = useDispatch()
  const users = useSelector(state => state.users.users)

  useEffect(() => {
    dispatch(fetchUsers())
  }, [dispatch])

  return (
    <div className="App">
     <Form />
       <h2> Users</h2>
     <div>
        {users && users.map((user, index) => {
          return (
            <div key={index}>
               <p>{user.email}</p>
               <p>{user.name}</p>
            </div>
          )
        })}
     </div>
    </div>
  );
}

export default App;
