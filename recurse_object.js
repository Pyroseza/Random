var obj = {
  a: 'value1',
  b: 'value2',
  c: 'value3',
  d: 'value4',
  e: ['value5', 'value6', "value7"],
  f: {
    g: 'value8',
    h: ['value9'],
    i: {
      j: 'value10'
    }
  }
};

traverse = obj => {
  Object.keys(obj).forEach(function(key, idx) {
    objType = typeof obj[key];
    if (objType === typeof {} || objType === typeof []) {
      traverse(obj[key]);
    } else {
      window.document.write(typeof key + ' ' + key + ": " + typeof obj[key] + ' '+ obj[key] + '\n');
    }
  });

}

traverse(obj);
