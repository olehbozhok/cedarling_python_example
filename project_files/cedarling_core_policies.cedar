// simple policy example for pricipal workload
permit (
    principal is Jans::Workload,
    action in [Jans::Action::"Update"],
    resource is Jans::Issue
)
when { principal.org_id == resource.org_id };

// simple policy example for pricipal user
permit (
    principal is Jans::User,
    action in [Jans::Action::"Update"],
    resource is Jans::Issue
)
when { principal.country == resource.country };

// simple policy example for pricipal role
permit (
    principal == Jans::Role::"Admin",
    action in [Jans::Action::"Update"],
    resource is Jans::Issue
);