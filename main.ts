// Entrypoint for the 18 November news-image entry.
// Reads the picture stored next to this script, sanity-checks it,
// and places a copy in the folder the grader expects to find it in.

import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const LIMIT_BYTES = 1_048_576;
const PNG_MAGIC = [0x89, 0x50, 0x4e, 0x47];
const JPEG_MAGIC = [0xff, 0xd8, 0xff];

function fail(reason: string): never {
  throw new Error(`news-image entry: ${reason}`);
}

function startsWith(data: Buffer, magic: number[]): boolean {
  if (data.length < magic.length) return false;
  return magic.every((byte, index) => data[index] === byte);
}

function looksLikeImage(data: Buffer): boolean {
  return startsWith(data, PNG_MAGIC) || startsWith(data, JPEG_MAGIC);
}

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const sourcePath = path.resolve(scriptDir, "entry.png");

if (!existsSync(sourcePath)) {
  fail(`missing source picture at ${sourcePath}`);
}

const picture = readFileSync(sourcePath);

if (!looksLikeImage(picture)) {
  fail("source picture is neither PNG nor JPEG (bad leading bytes)");
}

if (picture.byteLength > LIMIT_BYTES) {
  fail(`source picture is ${picture.byteLength} bytes, over the ${LIMIT_BYTES} byte cap`);
}

const targetDir = process.env.MAKEFUN_OUTPUT_DIR
  ? path.resolve(process.env.MAKEFUN_OUTPUT_DIR)
  : "/output";
const targetPath = path.resolve(targetDir, "entry.png");

mkdirSync(targetDir, { recursive: true });
writeFileSync(targetPath, picture);

console.log(`Wrote ${picture.byteLength} bytes to ${targetPath}`);
