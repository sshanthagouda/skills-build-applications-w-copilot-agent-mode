import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Workouts API endpoint:', endpoint);
        console.log('Fetched workouts:', data);
        setWorkouts(data.results || data);
      });
  }, [endpoint]);

  return (
    <div className="card">
      <div className="card-body">
        <h2 className="card-title">Workouts</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Name</th>
              <th>Suggested For</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout, idx) => (
              <tr key={idx}>
                <td>{workout.name}</td>
                <td>{Array.isArray(workout.suggested_for) ? workout.suggested_for.join(', ') : workout.suggested_for}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Workouts;
