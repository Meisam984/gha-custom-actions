const core = require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');

function run() {
  // 1) Get some input values
  const bucket = core.getInput('bucket', { required: true });
  const bucketRegion = core.getInput('bucket-region', { required: true });
  const distFolder = core.getInput('dist-folder', { required: true });

  // 2) Upload files within dist-folder
  const s3URI = `s3://${bucket}`
  exec.exec(`aws s3 sync ${distFolder} ${s3URI} --region ${bucketRegion}`);

  const websiteURL = `http://${bucket}.s3-website.${bucketRegion}.amazonaws.com`;
  core.setOutput('website-url', websiteURL);
}

run();