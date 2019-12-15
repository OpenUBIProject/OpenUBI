async function getCandidateJSON(filename, stateKey) {
  let response = await fetch(`./static/assets/${filename}.json`);
  let json = await response.json()
  if (filename === 'president') {
    return json;
  } else {
    return json.filter((candidate) => candidate['Best DIST'].substring(0, 2) === stateKey);
  };
};

function getCandidatePolicyStanceImage(stance) {
  let imgUrl;
  let altText;

  if (stance === '0') {
    imgUrl = 'https://raw.githubusercontent.com/joezippy/OpenUBI/master/project-images/red-x.png?raw=true';
    altText = 'No'
  } else if (stance === '1') {
    imgUrl = 'https://github.com/joezippy/OpenUBI/blob/master/project-images/green-check.png?raw=true';
    altText = 'Yes'
  } else {
    imgUrl = 'https://github.com/joezippy/OpenUBI/blob/master/project-images/question-mark.png?raw=true';
    altText = 'N/A'
  };

  return `<img src=${imgUrl} alt=${altText}></img>`
};

async function queryCandidates(stateKey) {
  console.log(stateKey);
  let filenames = ['president', 'house', 'senate'];

  for (let filename of filenames) {
    let candidatesJSON = await getCandidateJSON(filename, stateKey);
    let tableBody = $(`#table-${filename} tbody`);
    let tableEntries = '';

    if (candidatesJSON.length === 0) {
      tableBody.html('No candidates found');
      return;
    };

    for (let candidate of candidatesJSON) {
      let candidateDist = candidate['Best DIST'];
      let candidateName = candidate['Best Name'];
      let candidateParty = candidate['Best Party'];
      let candidateTwitterUsername = candidate['Twitter'];
      let isUbiCaucusMember = getCandidatePolicyStanceImage(candidate['UBI']);
      let fifteenDollarMinimumWage = getCandidatePolicyStanceImage(candidate['15MIN']);
      let medicareForAll = getCandidatePolicyStanceImage(candidate['M4A']);
      let greenNewDeal = getCandidatePolicyStanceImage(candidate['GND']);
      let collegeForAll = getCandidatePolicyStanceImage(candidate['C4A']);
      let noCorporatePAC = getCandidatePolicyStanceImage(candidate['No Corp']);

      tableEntries +=
      `
        <tr>
          <th width="260px">
            ${candidateDist}
          </th>
          <th>
          </th>
        </tr>
        <tr>
          <td width="260px">
            Candidate
          </td>
          <td>
            ${candidateName} - (${candidateParty})
          </td>
        </tr>
        <tr>
          <td width="260px">
            Twitter Username
          </td>
          <td>
            <a href="https://twitter.com/${candidateTwitterUsername}" target="_blank">
              ${candidateTwitterUsername}
            </a>
          </td>
          </tr>
          <tr>
            <td width="260px">
              UBI Caucus Member
            </td>
            <td>
              ${isUbiCaucusMember}
            </td>
          </tr>
          <tr>
            <td width="260px">
              $15 Minimum Wage (or better)
            </td>
            <td>
              ${fifteenDollarMinimumWage}
            </td>
          </tr>
          <tr>
            <td width="260px">
              Medicare for All
            </td>
            <td>
              ${medicareForAll}
            </td>
          </tr>
          <tr>
            <td width="260px">
              Green New Deal
            </td>
            <td>
              ${greenNewDeal}
            </td>
          </tr>
          <tr>
            <td width="260px">
              Public College for All
            </td>
            <td>
              ${collegeForAll}
            </td>
          </tr>
          <tr>
            <td width="260px">
              No Corporate PAC Money
            </td>
            <td>
              ${noCorporatePAC}
            </td>
          </tr>
    `
    };

    tableBody.html(tableEntries);
  };
};
