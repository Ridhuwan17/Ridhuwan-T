const jwt = require('jsonwebtoken');

async function checkRole(req, res, next) {
    // Get the token from the header
    const token = req.headers['authorization'];

    // Check if token exists
    if (!token) {
        return res.status(403).send({ auth: false, message: 'No token provided.' });
    }

    // Verify the token
    jwt.verify(token, 'uSeRPasSkEy', function(err, decoded) {
        if (err) {
            return res.status(500).send({ auth: false, message: 'Failed to authenticate token.' });
        }

        // Check the user role
        if (decoded.role === 'player') {
            // Pass the control to the next middleware function
            next();
        } else {
            return res.status(401).send({ auth: false, message: 'Unauthorized role.' });
        }
    });
}

async function checkSession(req, res, next) {
    if (req.session.token) {
      console.log('User in session: ', req.session.token);
      next();
    } else {
      res.status(401).send({ auth: false, message: 'No user in session.' });
    }
  }

module.exports = {checkRole,checkSession};