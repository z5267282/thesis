// Provide 'remote' as the first command-line argument if you want the remote server to be used.
// The local server is used by default.

let local = true;
if (process.argv.length >= 3 && process.argv[2] === 'remote') {
    local = false;
}

process.env.REACT_APP_HOST = (local) ? 'LOCAL' : 'REMOTE';
// ensure that the front end does not auto-open browser
process.env.BROWSER = 'none';

require('react-scripts/scripts/start');
