# Reading Path: Implementer & Engineering Team

**For:** Developers, backend engineers, mobile/web engineers, DevOps engineers, QA engineers  
**Focus:** Protocols, APIs, data formats, implementation details, testing strategy, deployment  
**Time:** 60–90 minutes to read; 2–3 hours with spec review and coding exercises  
**Outcome:** Understand what you need to build, protocol flows, data formats, testing requirements

---

## Before You Start

**You should know:**
- Your programming language/platform (Python, Node.js, Swift, etc.)
- HTTP APIs and REST concepts
- Basic cryptography (what a signature is, what encryption is)
- JSON and data serialization formats
- Your team's development process

**You might skip if:**
- You're designing system architecture (see [Architect path](./reading-path-architect.md))
- You're focused on governance/compliance (see [Policy path](./reading-path-policy-leadership.md))

---

## Key Concepts for Implementers

### 1. You're Implementing One of Three Roles

**Choose yours:**

```
[ ] Wallet Provider (backend services)
    → API endpoints, credential storage, audit logging
    
[ ] Wallet Instance Developer (app/web)
    → UI, user authentication, credential display, key management
    
[ ] Service Integration (Relying Party)
    → API calls to wallet, credential verification, authentication logic
```

**ARF applies to all, but implementation details differ.**

### 2. Protocols Are the Interface

You mainly work with three protocols:

| Protocol | Direction | Use Case | Spec |
|----------|-----------|----------|------|
| **OpenID4VCI** | Issuer → Wallet | Getting credentials | [openid.net spec](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) |
| **OpenID4VP** | Wallet → Service | Proving credentials | [openid.net spec](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) |
| **HAIP** | Wallet ↔ Reader | NFC proximity | ARF proprietary |

**Your job:** Implement these as client or server.

### 3. Credentials Are Data

Credentials are digitally signed JSON structures. Example:

```json
{
  "header": {
    "alg": "RS256",
    "typ": "JWT"
  },
  "payload": {
    "iss": "https://government.example/pid",
    "sub": "user123",
    "given_name": "Alice",
    "family_name": "Smith",
    "birthdate": "1990-01-01",
    "device_key": "[public key]",  // if device binding
    "exp": 1735689600
  },
  "signature": "[base64 signature]"
}
```

**Your job:** Parse, verify, and store these securely.

### 4. Security Is Non-Negotiable

ARF requires:
- Private keys in secure storage (no exporting)
- User authentication before sharing credentials
- Audit logging of all operations
- Encrypted data at rest
- HTTPS for all API calls

**Your job:** Implement these from day one, not as an afterthought.

### 5. Testing Means Evidence

You need test evidence for certification:
- Unit tests (code behavior)
- Integration tests (flows end-to-end)
- Security tests (can keys be extracted?)
- Interoperability tests (work with other wallets/services?)

**Your job:** Write tests that prove conformance.

---

## Recommended Reading Order

### Section 1: ARF Implementation Overview (10 min)

**Read:** [ARF Explained](../arf-explained.md) → "Key Scenarios" section

**Then:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 5** (Data Flows)

**Key Questions to Answer:**
- [ ] What are the main data flows (issuance, presentation, registration)?
- [ ] What are the roles in each flow?
- [ ] What APIs/protocols are involved?

---

### Section 2: Choose Your Role & Read Specific Sections (15 min)

**If Wallet Provider (Backend):**
- **Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 4, Sections 4.1 (Ecosystem), 4.4 (Lifecycle)
- **Focus on:** Credential storage, issuance endpoints, audit logging
- **Key Questions:**
  - [ ] How are credentials stored and retrieved?
  - [ ] What APIs must I expose (issuance, revocation, metadata)?
  - [ ] What audit logs are required?

**If Wallet Instance (App/Web):**
- **Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 3 (Architecture), Chapter 5 (Flows)
- **Focus on:** Key management, UI flows, credential display
- **Key Questions:**
  - [ ] How do I handle user authentication (biometric, PIN)?
  - [ ] How do I display the credential request to users?
  - [ ] Where do I store keys (Secure Enclave, encrypted local)?

**If Service Integration (Relying Party):**
- **Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 4, Section 4.5 (Relying Parties), Chapter 5, Sections 5.2–5.3 (Remote flows)
- **Focus on:** Credential request creation, signature verification, registration
- **Key Questions:**
  - [ ] How do I create a credential request?
  - [ ] How do I verify the wallet's response?
  - [ ] How do I integrate with wallets across the EU?

---

### Section 3: Understand Protocol Flows (20 min)

**Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 5** in detail

**Then:** Review [Quick Reference](../quick-reference.md) → Protocol links

**For Each Protocol:**

| Protocol | Read | Focus |
|----------|------|-------|
| **OpenID4VCI** | [Spec](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) | Authorization code flow, credential endpoint, token request |
| **OpenID4VP** | [Spec](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) | Presentation request, wallet response, verification |
| **HAIP** | ARF Section 5.1.2 | NFC communication, device authorization |

**Key Questions to Answer:**
- [ ] What are the steps in credential issuance (OpenID4VCI)?
- [ ] What are the steps in credential presentation (OpenID4VP)?
- [ ] What is the difference between authorization code and pushed credential flow?

---

### Section 4: Data Formats & Serialization (15 min)

**Read:** [Conformance Interpretation Companion](../conformance-interpretation-companion.md) → "Evidence Types & Collection" → "Data Format" section

**Then:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 4, Section 4.2 (Attestations)

**Also:** Rulebooks for credentials you support
- **PID Rulebook:** https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog
- **Other Rulebooks:** Check the catalog

**Key Questions to Answer:**
- [ ] What credential formats are supported (SD-JWT, CWT, JSON)?
- [ ] What are the required and optional claims for each credential type?
- [ ] How are credentials serialized for storage and transmission?

---

### Section 5: Security & Cryptography (15 min)

**Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 6** (Security, Integrity)

**Then:** [Governance to Control Mapping](../governance-to-control-mapping.md) → "Cryptographic Controls" pattern

**Key Questions to Answer:**
- [ ] What cryptographic algorithms are required (RS256, ECDSA)?
- [ ] How must private keys be stored (Secure Enclave, encrypted database)?
- [ ] What authentication is required before using keys?
- [ ] How do I verify issuer signatures?

---

### Section 6: Testing & Certification (10 min)

**Read:** [Conformance Interpretation Companion](../conformance-interpretation-companion.md) → "Conformance Assessment Framework" sections 1–5

**Then:** [Conformance Interpretation Companion](../conformance-interpretation-companion.md) → "Evidence Types & Collection"

**Key Questions to Answer:**
- [ ] What tests must I write to prove conformance?
- [ ] What evidence is needed for certification?
- [ ] How do I structure a test plan?

---

## Deep-Dive Topics (Optional)

### If You're Building Wallet Provider APIs

**Additional Reading:**
1. [OpenID4VCI Spec](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) — Full protocol
2. [CIR 2024/2980](https://data.europa.eu/eli/reg_impl/2024/2980/oj) → Ecosystem notifications
3. [CIR 2024/2982](https://data.europa.eu/eli/reg_impl/2024/2982/oj) → Protocols and interfaces

**Implementation Topics:**
- Authorization server (OAuth2)
- Credential endpoint (issuing credentials)
- Metadata endpoint (wallet discovery)
- Revocation endpoint (revocation status)
- Audit logging (all operations)

**Sample Endpoints:**
```
POST /oauth2/token          (issue access token)
POST /credentials           (issue credential)
GET /.well-known/openid-credential-issuer
GET /revocation-status      (check if revoked)
POST /audit-log             (log operations)
```

---

### If You're Building Wallet App/Web

**Additional Reading:**
1. [OpenID4VCI Spec](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) — Client side
2. [OpenID4VP Spec](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) — Client side
3. Platform guides: iOS Secure Enclave, Android TEE, Web Crypto API

**Implementation Topics:**
- Enrollment (getting first credentials from issuer)
- Key management (generating, storing, using keys)
- Credential storage (database, encryption)
- Presentation flow (responding to service requests)
- User authentication (biometric, PIN, device unlock)

**Sample Flows:**
```
1. Enrollment:
   User → Opens wallet → Clicks "Add government ID"
   → Wallet opens issuer website
   → Wallet receives OpenID4VCI request
   → Wallet opens authorization flow
   → Issuer returns signed credential
   → Wallet stores in secure database

2. Authentication:
   Service → Shows QR code
   User → Scans QR
   Wallet → Parses OpenID4VP request
   → Shows "Service wants your name and birthdate"
   → User taps "Approve"
   → User provides biometric/PIN
   → Wallet signs response with private key
   → Wallet sends response to service
```

---

### If You're Integrating a Service (Relying Party)

**Additional Reading:**
1. [OpenID4VP Spec](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) — Full protocol
2. [CIR 2025/848](https://data.europa.eu/eli/reg_impl/2025/848/oj) → RP registration
3. [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 4, Section 4.5 (Relying Party responsibilities)

**Implementation Topics:**
- Metadata endpoint (advertising your service)
- Presentation request creation (OpenID4VP)
- Response handling (receiving wallet's credential)
- Signature verification (using issuer public key)
- User mapping (linking credential to your user)

**Sample Endpoints:**
```
GET /.well-known/openid-relying-party    (service metadata)
POST /auth/request                       (create auth request)
POST /auth/response                      (receive credential)
```

---

## Implementation Patterns

### Pattern 1: Wallet Provider Issuance

```python
# Pseudo-code: Issuing a credential

@app.route('/credentials', methods=['POST'])
def issue_credential(request):
    # 1. Verify authorization (access token valid?)
    token = verify_access_token(request.headers['Authorization'])
    
    # 2. Parse credential request
    cred_request = request.json
    
    # 3. Prepare credential claims
    claims = {
        'iss': 'https://government.example/pid',
        'sub': token.user_id,
        'given_name': get_user_data('given_name'),
        'family_name': get_user_data('family_name'),
        'birthdate': get_user_data('birthdate'),
        'device_key': cred_request.get('device_public_key'),  # if device binding
        'exp': int(time.time()) + (365 * 24 * 60 * 60)  # 1 year
    }
    
    # 4. Sign credential with issuer private key
    credential = jwt.encode(claims, ISSUER_PRIVATE_KEY, 'RS256')
    
    # 5. Return in requested format
    return {
        'credential': credential,
        'format': 'jwt'
    }
```

---

### Pattern 2: Wallet App Key Management

```swift
// Pseudo-code: Storing credential with device binding

func storeCredential(credential: String, issuer: String) {
    // 1. Generate device key pair on Secure Enclave
    let deviceKey = SecKeyCreateRandomKey(
        [.class: kSecAttrKeyClassPrivate,
         .type: kSecAttrKeyTypeRSA,
         .keySizeInBits: 2048],
        nil)
    
    // 2. Extract public key (for credential binding)
    let publicKey = SecKeyCopyPublicKey(deviceKey)!
    
    // 3. Store credential in secure database
    let credential = Credential(
        jwt: credential,
        issuer: issuer,
        devicePublicKey: publicKey,
        createdAt: Date()
    )
    
    // 4. Save to encrypted local database
    try secureDatabase.save(credential)
    
    // Note: Private key stays on Secure Enclave,
    // never exported or backed up unencrypted
}
```

---

### Pattern 3: Service Verification

```python
# Pseudo-code: Verifying wallet response

def verify_credential_response(response):
    # 1. Parse the credential (JWT)
    credential = jwt.decode(response.credential, options={"verify_signature": False})
    
    # 2. Get issuer public key from trust list
    issuer_url = credential['iss']
    issuer_key = get_issuer_public_key(issuer_url)
    
    # 3. Verify credential signature
    try:
        decoded = jwt.decode(response.credential, issuer_key, algorithms=['RS256'])
    except jwt.InvalidSignatureError:
        return False  # Invalid signature
    
    # 4. Check expiration
    if decoded['exp'] < time.time():
        return False  # Expired
    
    # 5. Check revocation (if revocation endpoint available)
    if is_revoked(issuer_url, decoded['jti']):
        return False  # Revoked
    
    # 6. Verify device binding (if present)
    if 'device_key' in decoded:
        if not verify_device_signature(response.device_proof, decoded['device_key']):
            return False  # Device proof invalid
    
    # 7. Extract claims (name, birthdate, etc.)
    claims = {
        'given_name': decoded['given_name'],
        'family_name': decoded['family_name'],
        'birthdate': decoded['birthdate']
    }
    
    return True, claims
```

---

## Testing Checklist

### Unit Tests (Minimum)

- [ ] Can I serialize credentials correctly?
- [ ] Can I parse incoming credentials?
- [ ] Can I generate and verify signatures?
- [ ] Can I encrypt/decrypt data?
- [ ] Can I handle key storage and retrieval?
- [ ] Can I validate JWT structure?
- [ ] Can I check expiration dates?

### Integration Tests

- [ ] Can I complete issuance flow end-to-end?
- [ ] Can I complete presentation flow end-to-end?
- [ ] Can I register with issuer metadata service?
- [ ] Can I handle credential revocation?
- [ ] Can I verify signatures from multiple issuers?

### Security Tests

- [ ] Can I extract private keys? (Should fail)
- [ ] Can I use credentials without user approval? (Should fail)
- [ ] Can I tamper with credentials? (Detection should work)
- [ ] Can I use credential on different device? (Should fail if device binding)

### Interoperability Tests

- [ ] Does my wallet accept credentials from reference implementation?
- [ ] Does reference implementation accept my credentials?
- [ ] Can my service verify wallets from other vendors?
- [ ] Can I handle different credential formats (SD-JWT, CWT)?

---

## Development Environment Setup

### Local Testing

```bash
# 1. Set up test issuer (mock OpenID4VCI server)
docker run -p 8080:8080 eu-wallet-test-issuer

# 2. Set up test verifier (mock OpenID4VP server)
docker run -p 8081:8081 eu-wallet-test-verifier

# 3. Download test vectors (crypto test cases)
git clone https://github.com/eu-digital-identity-wallet/test-vectors

# 4. Install libraries
npm install oauth4webapi  # JavaScript OAuth client
pip install authlib       # Python OAuth
swift package add https://github.com/auth0/JwtKit  # Swift JWT
```

### CI/CD Integration

```yaml
# GitHub Actions example
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run unit tests
        run: npm test
      - name: Run integration tests
        run: npm run test:integration
      - name: Run security tests
        run: npm run test:security
      - name: Upload coverage
        run: npm run coverage
```

---

## Common Implementation Questions

### Q1: "Where do I store the wallet's private key?"

**A:** It depends on your platform:

| Platform | Storage | How |
|----------|---------|-----|
| **iOS** | Secure Enclave | Use `SecKeyCreateRandomKey()` |
| **Android** | TEE (Trusted Execution Environment) | Use `AndroidKeyStore` |
| **Web** | Encrypted Local Storage | Use `crypto.subtle.wrapKey()` |
| **Server** | HSM (Hardware Security Module) | Use PKCS#11 |

**Rule:** Private key must never be exported or accessible to application code.

---

### Q2: "How do I handle user authentication before sharing credentials?"

**A:** Implement multi-step verification:

```
1. User sees request: "Service wants your name and birthdate"
2. User taps "Approve"
3. System prompts for biometric or PIN
4. After successful authentication → Unlock key and sign response
5. Send signed response to service
```

**Implementation:**
- iOS: `LAContext.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics)`
- Android: `BiometricPrompt.authenticate()`
- Web: Fallback to strong password or security key

---

### Q3: "How do I support both on-device and cloud keys?"

**A:** Design a key abstraction:

```
KeyProvider interface
  ├─ LocalKeyProvider (on-device, Secure Enclave)
  ├─ CloudKeyProvider (cloud, encrypted backup)
  └─ HybridKeyProvider (use both)

When signing:
  - If device available → Use local key
  - If device unavailable → Use cloud backup (encrypted)
  - User decides which to use
```

---

### Q4: "What's the difference between SD-JWT and CWT?"

**A:**

| Format | Type | Use Case | Size |
|--------|------|----------|------|
| **SD-JWT** | Text-based (JSON) | Web, JSON APIs | Larger (~1 KB) |
| **CWT** | Binary (CBOR) | Mobile, NFC | Smaller (~300 bytes) |

**In ARF:** Both are allowed. Choose based on your use case.

---

### Q5: "How do I test against the ARF test suite?"

**A:** The ARF community provides:
- Test vectors (crypto test cases)
- Reference implementations (GitHub)
- Interop test events (annual EU testing)

**Steps:**
1. Download test vectors from [ARF repo](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework)
2. Run your implementation against them
3. Compare output
4. Participate in annual interop event (if public)

---

## Code Examples & References

### OpenID4VCI Implementation

**JavaScript:**
```javascript
import { createServer } from 'oauth4webapi';

const issuer = await createServer(ISSUER_URL);
const client = {
  client_id: 'my-wallet',
  redirect_uris: ['app://callback']
};

// Request credential
const response = await issuer.credential(client, accessToken, {
  format: 'jwt',
  proof: { jwt: deviceProof }
});
```

**Python:**
```python
from authlib.oauth2 import OAuth2Session

session = OAuth2Session(client_id='my-wallet')
token = session.fetch_token(issuer_token_endpoint, code=auth_code)
credential = requests.post(issuer_credential_endpoint,
    json={'format': 'jwt'},
    headers={'Authorization': f'Bearer {token}'}
).json()
```

---

## Next Steps

1. **Choose your role** (Provider, Instance, Service)
2. **Review protocol specs** for your role
3. **Download test vectors** from ARF repository
4. **Implement minimum features** (credential store, issuance, verification)
5. **Write unit tests** to prove behavior
6. **Participate in interop testing** if available
7. **Plan for certification** using [Conformance Interpretation Companion](../conformance-interpretation-companion.md)

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
