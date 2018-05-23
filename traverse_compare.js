var obj = {
  a: 'value1',
  b: 'value2',
  c: {
    d: 'value3',
    e: 'value4'
  },
  f: {
    g: 'value5',
    h: 'value6'
  }
};

var fil = {
  a: '',
  b: '',
  c: {
    d: 'value3',
    e: ''
  },
  f: {
    g: '',
    h: ''
  },
  i: 'asdf'
};

traverse = (fil, obj, level = 1) => {
  let res = null;
  Object.keys(fil).forEach(function(key, idx) {
    res = null;
    objType = typeof fil[key];
    if (objType === typeof {} || objType === typeof []) {
      traverse(fil[key], obj[key], ++level);
      --level;
    } else {
      if (!!fil[key]) {
        // filter is set
        // check if obj exists
        if (obj[key] === undefined) {
          //
          window.console.write(obj[key] + '<br />');
        } else {
          if (fil[key] === obj[key].toString()) {
            res = true;
          } else {
            res = false;
          }
          window.document.write('--'.repeat(level) + ' ' + !!fil[key] + '=' + fil[key] + ' => ' + obj[key] + ' ' + obj[key] + '<br />');
        }
      } else {
        // filter is not set
        res = null;
      }
    }
  });

}

traverse(fil, obj);
