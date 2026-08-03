import { jwtVerify, SignJWT } from 'jose';

export const CMS_SESSION_COOKIE = 'cms_admin_session';
const THIRTY_DAYS_MS = 1000 * 60 * 60 * 24 * 30;

export type CmsSessionPayload = {
  sub: string;
  email: string;
  role: 'admin' | 'editor';
  name: string;
};

function getSecret() {
  const value = process.env.JWT_SECRET;
  if (!value) throw new Error('JWT_SECRET is required for CMS auth');
  return new TextEncoder().encode(value);
}

export async function issueCmsSession(payload: CmsSessionPayload) {
  return new SignJWT({ email: payload.email, role: payload.role, name: payload.name })
    .setProtectedHeader({ alg: 'HS256' })
    .setSubject(payload.sub)
    .setIssuedAt()
    .setExpirationTime('30d')
    .sign(getSecret());
}

export async function verifyCmsSession(token: string) {
  const verified = await jwtVerify(token, getSecret());
  return verified.payload as unknown as CmsSessionPayload & { sub: string };
}

export function getCmsSessionMaxAge() {
  return THIRTY_DAYS_MS;
}
